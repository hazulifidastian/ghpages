################################
Random Points Django dan Postgis
################################

:date: 2019-09-01 09:00
:author: Hazuli Fidastian
:tags: django ; postgis
:lang: id
:status: draft

.. code-block:: python

   from django.db import connection

   with connection.cursor() as cursor:
       cursor.execute(
           f"""
           SELECT (
               ST_Dump(
                   ST_GeneratePoints(
                       (select kolom_polygon from table_berisi_polygon where id = 1),
                       {jumlah_point}
                   )
                )
           ).geom;
           """
       )
       points = cursor.fetchall()  # List of tuple
    
   for point in points:
       print(point.0)
