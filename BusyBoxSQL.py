#! /usr/bin/python3.7
#
# author: Krzysztof Czarnecki
# email: czarnecki.krzysiek@gmail.com
# opensource licence: GPL-3.0
# application: GLOBSIM

import os, sys
import sqlite3
import ToolBox
import VectorDiagram

class BusyBoxSQL:
    __ints = ["map_width", "map_height", "map_project"]
    
    def __init__(self, fname):
        if not os.path.exists(fname):
            ToolBox.print_error(f"path {fname} not exists!")
            sys.exit(-1)
        self.db_name = fname
            
        def dict_factory(cur, row):
            gen = enumerate(cur.description)
            out = {c[0]: row[i] for i,c in gen}
            return out

        self.conn = sqlite3.connect(fname)
        self.conn.row_factory = dict_factory
        self.cur = self.conn.cursor()

    def __del__(self):
        try:
            self.conn.commit()
            self.conn.close()
        except AttributeError:
            pass
        
    def execute(self, query):        
        self.cur.execute(query)
        return self.cur.fetchall()

    ###
    ### config specific
    ###
    
    def get_config_by_name(self, name):
        out = self.execute(f"SELECT value FROM config WHERE name='{name}'")
        assert len(out) == 1, "(e) outlen != 1"
        if name in self.__ints:
            return int(out[0]["value"])
        else: return out[0]["value"]

    def set_config_by_name(self, name, value):
        self.execute(f"UPDATE config SET value={value} WHERE name='{name}'")
        if self.cur.rowcount == 0:
            self.execute(f"INSERT INTO config(name, value) VALUES ('{name}', {value})")
        
    def delete_config_by_name(self, name):
        self.execute(f"DELETE FROM config WHERE name='{name}'")

    def get_config_as_dict(self):
        out = self.execute("SELECT * FROM config")
        assert len(out) > 0, "(e) config length < 1"

        dout = {}
        for drow in out:
            if drow['name'] in self.__ints:                
                dout[drow['name']] = int(drow['value'])
            else: dout[drow['name']] = drow['value']
        return dout

    ###
    ### terrain specific
    ###

    def get_colors_as_list(self):
        out = self.execute(f"SELECT color FROM terrain")
        return [drow["color"] for drow in out]

    def get_terrain_as_dict(self, color):
        out = self.execute(f"SELECT * FROM terrain WHERE color='{color}'")
        assert len(out) == 1, "(e) only 1 terrain is expected"
        return out[0]

    ###
    ### diagram specific
    ###

    def get_node_names_as_set(self):
        out = self.execute("SELECT node FROM diagram")
        assert len(out) > 0, "(e) node number < 1"
        nodeset = set()
        for drow in out:
            nodeset.add(drow["node"])
        return nodeset
        
    def get_vector_diagram(self):
        dout = self.execute("SELECT * FROM diagram")
        assert len(dout) > 0, "(e) diagram length < 1"
        tout = self.execute("SELECT * FROM terrain")
        assert len(tout) > 0, "(e) terrains number < 1"
        cout = self.execute("SELECT * FROM config")
        assert len(cout) > 0, "(e) config length < 1"
        return VectorDiagram.VectorDiagram(dout, cout, tout)

    def get_node_coordinates_as_set(self, node):
        out = self.execute(f"SELECT x, y FROM diagram WHERE node='{node}'")
        assert len(out) > 0, "(e) node atom number < 1"

        xyset = set()
        for drow in out:
            item = drow["x"], drow["y"]
            xyset.add(item)
        return xyset

    def get_node_atoms_as_dict(self, node):
        out = self.execute(f"SELECT * FROM diagram WHERE node='{node}'")
        assert len(out) > 0, "(e) node atom number < 1"
        
        atoms = {}
        for drow in out:
            item = drow["x"], drow["y"]
            atoms[item] = drow["color"], drow["dx"], drow["dy"]
        return atoms

    def set_node_by_coordinates(self, x, y, node):
        self.execute(f"UPDATE diagram SET node='{node}' WHERE x={x} AND y={y}")
        self.conn.commit()

    def set_color_by_coordinates(self, x, y, color):
        self.execute(f"UPDATE diagram SET color='{color}' WHERE x={x} AND y={y}")
        self.conn.commit()