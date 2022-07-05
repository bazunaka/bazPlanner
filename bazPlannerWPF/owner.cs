using System;
using System.Data.SQLite;
using static bazPlannerWPF.sqlite_connect;

namespace bazPlannerWPF
{
    public class Owner
    {
        public string nameOwner;
        public string passwordOwner;

        public void AddToDatabase(string nameOwner, string passwordOwner)
        {
            InsertUser(nameOwner, passwordOwner);
        }
        static public void CheckAdmin()
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = "SELECT * FROM owner WHERE name_owner='admin'"
            };
            int cnt = command.ExecuteReader().StepCount;
            if (cnt == 1)
            {
                auth form_auth = new auth();
                form_auth.Show();
            }
        }
    }
}
