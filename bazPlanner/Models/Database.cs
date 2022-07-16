using System.Data.SQLite;
using System.Diagnostics;

namespace bazPlanner.Models
{
    class Database
    {
        //Create connection.
        static public bool Connect()
        {
            try
            {
                var connectionStringBuilder = new SQLiteConnectionStringBuilder();
                connectionStringBuilder.DataSource = "test.db";

                using (var connection = new SQLiteConnection(connectionStringBuilder.ConnectionString))
                {
                    connection.Open();
                }
                Debug.WriteLine("Connected!");
                return true;
            }
            catch (SQLiteException ex)
            {
                Debug.WriteLine($"Ошибка доступа к базе данных. Исключение: {ex.Message}");
                return false;
            }
            
        }            
    }
}
