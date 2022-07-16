using System.Windows;
using System.Data.SQLite;
using System.Diagnostics;

namespace bazPlanner
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            //Create connection.
            var connectionStringBuilder = new SQLiteConnectionStringBuilder();
            connectionStringBuilder.DataSource = "test.db";

            using (var connection = new SQLiteConnection(connectionStringBuilder.ConnectionString))
            {
                connection.Open();
                
                var selectCmd = connection.CreateCommand();
                selectCmd.CommandText = "SELECT * FROM Owners";
                using var reader = selectCmd.ExecuteReader();
                while (reader.Read())
                {
                    var result = reader.GetString(1);
                    Debug.WriteLine(result);
                }
            }
            Debug.WriteLine("Connected!");

           
            InitializeComponent();

        }
    }
}
